from .account_manager import AccountManager
from .serializers import AccountSerializer
from ..serializers import BsonSerializer
from ..models import Account
from djongo.models.fields import ObjectId
from utility.pagination_utilities import PaginationUtilities


class AccountImpl(AccountManager):

    account_id = None
    page = 1
    page_size = 10

    def __init__(self, account_id: str = None, page: int = 1, page_size: int = 10):
        self.set_account_id(account_id)
        self.page = page
        self.page_size = page_size

    def set_account_id(self, account_id):
        self.account_id = account_id

    def get_account_id(self):
        return self.account_id

    def fetch_all_accounts(self) -> dict:
        accounts = Account.objects.all()  # .filter(is_deleted=False)

        accounts = PaginationUtilities.paginate_results(accounts,
                                                        page_number=self.page,
                                                        page_size=self.page_size)

        account_data = AccountSerializer(accounts, many=True)

        response = {
            'success': True,
            'accounts': account_data.data
        }

        return response

    def fetch_account_by_id(self) -> dict:
        accounts = Account.get_object_or_raise_exception(self.get_account_id())

        account_data = AccountSerializer(accounts)

        response = {
            'success': True,
            'account': account_data.data
        }

        return response

    def create_account(self, data) -> dict:

        Account(**data).save()

        response = {
            'success': True,
        }

        return response

    def update_account(self, data) -> dict:

        Account.objects.filter(pk=ObjectId(self.get_account_id())).update(**data)

        response = {
            'success': True,
        }

        return response

    def delete_account(self) -> dict:
        account = Account.get_object_or_raise_exception(self.get_account_id())

        account.delete_account()

        response = {
            'success': True,
        }

        return response

    def search_account(self, query):

        accounts = [i for i in Account.objects.mongo_find(
            {'$or': [{'email': {"$regex": f'.*{query}.*', "$options": "i"}},
                     {'phone': {"$regex": f'.*{query}.*', "$options": "i"}}
                     ]
             }
        )]

        accounts = PaginationUtilities.paginate_results(accounts,
                                                        page_number=self.page,
                                                        page_size=self.page_size)

        data = BsonSerializer.serialize_search_results(accounts)

        response = {
            'success': True,
            'accounts': data
        }

        return response
