from rest_framework import serializers

# apiAPP এর model গুলো import করা হয়েছে
from apiAPP.models import Company, IceCream , Employe

# Company model এর জন্য serializer তৈরি করা হয়েছে
class CompanySerializer(serializers.HyperlinkedModelSerializer):

    Company_id = serializers.ReadOnlyField()
    class Meta:
        # কোন model এর জন্য serializer, সেটা বলা হয়েছে
        model = Company
        # সমস্ত field কে অন্তর্ভুক্ত করা হয়েছে
        fields = '__all__'

class EmployeeSerializers( serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:

        model = Employe
        fields = '__all__'
        
# IceCream model এর জন্য serializer তৈরি করা হয়েছে
class IceCreamSerializer(serializers.ModelSerializer):
    class Meta:
        # কোন model এর জন্য serializer, সেটা বলা হয়েছে
        model = IceCream
        # সমস্ত field কে অন্তর্ভুক্ত করা হয়েছে
        fields = '__all__'
