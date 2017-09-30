import logging
from rest_framework.views import APIView
from rest_framework.response import Response

from banks.models import Branches
from banks.serializers import BankBranchRequestSerailizer, APIResponseSerializer

# Create your views here.

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class BankDetails(APIView):
    def post(self, request):
        data = request.data
        if not data.get('ifsc_code'):
            return Response({"err_msg": "Missing/Empty parameter ifsc_code", "status": 400})
        import pdb
        pdb.set_trace()
        try:
            bank_set_data = Branches.objects.filter(ifsc=data.get('ifsc_code')).select_related('bank')
            response_data = []
            for bank_data in bank_set_data:
                res = bank_data.__dict__
                res['bank_name'] = bank_data.bank.name
                resp_data = APIResponseSerializer(data=res)
                if not resp_data.is_valid():
                    return Response({"err_msg": resp_data.errors, "status": 400})
                response_data.append(resp_data.data)
            return Response({"data": response_data, "status": 200})
        except Exception as e:
            logger.warn(str(e))
            return Response({"err_msg": "Kindly enter correct ifsc code.", "status": 400})


class BankBranchDetails(APIView):
    def post(self, request):
        data = request.data
        serialized_data = BankBranchRequestSerailizer(data=data)
        if not serialized_data.is_valid():
            return Response({"err_msg": serialized_data.errors, "status": 400})
        try:
            bank_set_data = Branches.objects.filter(city=serialized_data.data.get('city').upper(),
                                                    bank_id__name=serialized_data.data.get('bank_name').upper())
            response_data = []
            for bank_data in bank_set_data:
                res = bank_data.__dict__
                res['name'] = serialized_data.data.get('bank_name')
                resp_data = APIResponseSerializer(data=res)
                if not resp_data.is_valid():
                    return Response({"err_msg": resp_data.errors, "status": 400})
                response_data.append(resp_data.data)
            return Response({"data": response_data, "status": 200})
        except Exception as e:
            logger.warn(str(e))
            return Response({"err_msg": "Kindly enter correct ifsc code.", "status": 400})
