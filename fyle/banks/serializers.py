from rest_framework import serializers


class BankBranchRequestSerailizer(serializers.Serializer):
    city = serializers.CharField(max_length=50, required=True)
    bank_name = serializers.CharField(max_length=49, required=True)


class APIResponseSerializer(serializers.Serializer):
    city = serializers.CharField(max_length=50, required=False, allow_null=True, allow_blank=True)
    name = serializers.CharField(max_length=49, required=False, allow_null=True, allow_blank=True)
    ifsc = serializers.CharField(max_length=11, required=False, allow_null=True, allow_blank=True)
    state = serializers.CharField(max_length=26, required=False, allow_null=True, allow_blank=True)
    branch = serializers.CharField(max_length=74, required=False, allow_null=True, allow_blank=True)
    address = serializers.CharField(max_length=195, required=False, allow_null=True, allow_blank=True)
    district = serializers.CharField(max_length=50, required=False, allow_null=True, allow_blank=True)
