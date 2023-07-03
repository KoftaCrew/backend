import json
import requests
import threading
from rest_framework import serializers
from django.db import transaction

from exam.models import Exam
from model_answer.models import KeyPhrase, ModelAnswer
from student_answer.models import StudentAnswer, Answer
from grade.models import AnswerSegment
from Backend.settings import MODEL_URL


class StartGradingTriggerSerializer(serializers.ModelSerializer):
    mode = serializers.ChoiceField(Exam.ExamModes, required=False)

    class Meta:
        model = Exam
        fields = ['mode', ]

    def update(self, instance: Exam, validated_data: dict) -> Exam:
        instance.mode = 4
        instance.save()
        thread = threading.Thread(target=grade, args=(instance.id,))
        thread.start()
        return instance


@transaction.atomic
def grade(exam_id: int):
    submission_ids = StudentAnswer.objects.filter(exam_id=exam_id).values_list('id', flat=True)
    for submission in submission_ids:
        answers = Answer.objects.filter(student_answer_id=submission)
        for answer in answers:
            # Get Key Phrase Strings in list
            # Get Key Phrase ids in list
            # Get Max grades for key phrases in list
            model_answer_list = []
            model_answer_ids_list = []
            max_grades_list = []
            key_phrase_objects = answer.question.model_answer.model_answer_key_phrases.all()
            for key_phrase in key_phrase_objects:
                # Get string representation of model answer segmentation using indices of key phrase
                model_answer_list.append(get_text_segment(answer.question.model_answer, key_phrase))
                model_answer_ids_list.append(key_phrase.id)
                max_grades_list.append(key_phrase.grade)
            payload = json.dumps(
                {
                    "model_answer": model_answer_list,
                    "model_answer_ids": model_answer_ids_list,
                    "student_answer": answer.text,
                    "max_grades": max_grades_list
                }
            )
            headers = {
                'Content-Type': 'application/json'
            }
            url = MODEL_URL + "grade/"

            response = requests.request("POST", url, headers=headers, data=payload)
            if response.status_code == 200:
                response_dict: dict = response.json()
                total_grade = 0
                for i in range(0, len(response_dict.get('model_answer_ids', []))):
                    model_answer_id = response_dict.get('model_answer_ids')[i]
                    start_index = response_dict.get('segmented_student_answer')[i][0]
                    end_index = response_dict.get('segmented_student_answer')[i][1]
                    score = response_dict.get('scores')[i]
                    confidence = response_dict.get('confidence')[i]
                    total_grade += score
                    AnswerSegment.objects.create(
                        answer=answer,
                        key_phrase=KeyPhrase.objects.get(id=model_answer_id),
                        start_index=start_index,
                        end_index=end_index,
                        grade=score,
                        confidence=confidence
                    )

                answer.total_grade = total_grade
                answer.save()
    exam = Exam.objects.get(id=exam_id)
    exam.mode = 2
    exam.save()


def get_text_segment(model_answer_object: ModelAnswer, key_phrase_object: KeyPhrase) -> str:
    full_string: str = model_answer_object.text
    start_index: int = key_phrase_object.start_index
    end_index: int = key_phrase_object.end_index
    ret: str = ""
    for index in range(start_index, end_index):
        ret += full_string[index]
    return ret
