from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Skill, UserSkill
from .serializers import SkillSerializer, UserSkillSerializer


# GET all skills
@api_view(['GET'])
def list_skills(request):
    skills = Skill.objects.all()
    serializer = SkillSerializer(skills, many=True)
    return Response(serializer.data)


# CREATE skill (Admin use)
@api_view(['POST'])
def create_skill(request):
    serializer = SkillSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


# ADD skill to freelancer
@api_view(['POST'])
def add_user_skill(request):
    serializer = UserSkillSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response("Skill added to freelancer", status=201)
    return Response(serializer.errors, status=400)


# REMOVE skill from freelancer
@api_view(['DELETE'])
def remove_user_skill(request, id):
    try:
        user_skill = UserSkill.objects.get(id=id)
        user_skill.delete()
        return Response("Skill removed")
    except UserSkill.DoesNotExist:
        return Response("Not found", status=404)


# GET freelancer skills
@api_view(['GET'])
def freelancer_skills(request, user_id):
    skills = UserSkill.objects.filter(user_id=user_id)
    serializer = UserSkillSerializer(skills, many=True)
    return Response(serializer.data)
