from rest_framework import serializers
from modules.module_kholter.orm.model.kholter.kholter import Kholter

class KholterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kholter
        fields = '__all__'
