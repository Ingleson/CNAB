from rest_framework import generics
from .models import Transaction
from stores.models import Store
from .serializer import TransactionSerializer
from rest_framework.views import Response, Request, status
from datetime import datetime

class TransactionView(generics.ListCreateAPIView):
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()

    def create(self, request, *args, **kwargs):
        data = request.data['data']
        print(data)
        
        type = data[0]
        date = datetime.strptime(data[1:9], "%Y%m%d").date()
        value = float(data[9:19]) / 100
        cpf = data[19:30]
        card = data[30:42]
        hour = datetime.strptime(data[42:48], "%H%M%S").time()
        store_owner = data[48:62]
        store_name = data[62:]

        transaction = {
            "type": type,
            "date": date,
            "value": value,
            "cpf": cpf,
            "card": card,
            "hour": hour,
            "store_owner": store_owner,
            "store_name": store_name
        }

        store = Store.objects.get_or_create(
            store_name=store_name,
            store_owner=store_owner
        )

        if store[0].store_name == transaction['store_name']:
            if transaction['type'] in ["1", "4", "5", "6", "7", "8"]:
                store[0].balance += transaction['value']
            if transaction['type'] in ["2", "3", "9"]:
                store[0].balance += transaction['value'] * -1
        store[0].save()

        serializer = TransactionSerializer(data=transaction)
        serializer.is_valid(raise_exception=True)
        serializer.save(store=store[0])
        

        return Response(transaction, status.HTTP_201_CREATED)
