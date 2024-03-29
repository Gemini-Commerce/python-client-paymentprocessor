# coding: utf-8

"""
    Payment Processor Service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v1
    Contact: info@gemini-commerce.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from paymentprocessor.models.paymentprocessor_perform_refund_request import PaymentprocessorPerformRefundRequest

class TestPaymentprocessorPerformRefundRequest(unittest.TestCase):
    """PaymentprocessorPerformRefundRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PaymentprocessorPerformRefundRequest:
        """Test PaymentprocessorPerformRefundRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PaymentprocessorPerformRefundRequest`
        """
        model = PaymentprocessorPerformRefundRequest()
        if include_optional:
            return PaymentprocessorPerformRefundRequest(
                tenant_id = '',
                refund_id = '',
                payment = paymentprocessor.models.paymentprocessor_payment.paymentprocessorPayment(
                    id = '', 
                    code = '', 
                    additional_info = '', 
                    transactions = [
                        paymentprocessor.models.paymentprocessor_transaction.paymentprocessorTransaction(
                            payment_id = '', 
                            id = '', 
                            type = 'UNKNOWN', 
                            additional_info = '', 
                            child_transactions = [
                                paymentprocessor.models.paymentprocessor_transaction.paymentprocessorTransaction(
                                    payment_id = '', 
                                    id = '', 
                                    additional_info = '', )
                                ], )
                        ], ),
                amount = paymentprocessor.models.paymentprocessor_money.paymentprocessorMoney(
                    units = '', 
                    micros = 56, ),
                currency = 'XXX'
            )
        else:
            return PaymentprocessorPerformRefundRequest(
                tenant_id = '',
                refund_id = '',
                payment = paymentprocessor.models.paymentprocessor_payment.paymentprocessorPayment(
                    id = '', 
                    code = '', 
                    additional_info = '', 
                    transactions = [
                        paymentprocessor.models.paymentprocessor_transaction.paymentprocessorTransaction(
                            payment_id = '', 
                            id = '', 
                            type = 'UNKNOWN', 
                            additional_info = '', 
                            child_transactions = [
                                paymentprocessor.models.paymentprocessor_transaction.paymentprocessorTransaction(
                                    payment_id = '', 
                                    id = '', 
                                    additional_info = '', )
                                ], )
                        ], ),
        )
        """

    def testPaymentprocessorPerformRefundRequest(self):
        """Test PaymentprocessorPerformRefundRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
