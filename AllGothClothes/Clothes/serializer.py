from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from .models import *


class ClothModel: #класс, объексты которого будем преобразовывать в json строку
    def __init__(self, name, brand) -> None:
        self.name = name
        self.brand = brand


class ClothSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    brand = serializers.CharField()

def encode():
    model = ClothModel('THE HATE', 'hikikomori Kai')
    model_sr = ClothSerializer(model)
    print(model_sr.data, type(model_sr.data), sep='\n')
    json = JSONRenderer().render(model_sr.data)
    print(json)