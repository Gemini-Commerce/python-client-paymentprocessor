# coding: utf-8

"""
    Payment Processor Service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v1
    Contact: info@gemini-commerce.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictStr
from pydantic import Field
from paymentprocessor.models.paymentprocessor_currency import PaymentprocessorCurrency
from paymentprocessor.models.paymentprocessor_money import PaymentprocessorMoney
from paymentprocessor.models.paymentprocessor_payment_context import PaymentprocessorPaymentContext
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class PaymentprocessorInitPaymentRequest(BaseModel):
    """
    PaymentprocessorInitPaymentRequest
    """ # noqa: E501
    tenant_id: StrictStr = Field(alias="tenantId")
    context: Optional[PaymentprocessorPaymentContext] = None
    code: StrictStr
    amount: Optional[PaymentprocessorMoney] = None
    currency: Optional[PaymentprocessorCurrency] = None
    additional_info: Optional[StrictStr] = Field(default=None, alias="additionalInfo")
    __properties: ClassVar[List[str]] = ["tenantId", "context", "code", "amount", "currency", "additionalInfo"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of PaymentprocessorInitPaymentRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of context
        if self.context:
            _dict['context'] = self.context.to_dict()
        # override the default output from pydantic by calling `to_dict()` of amount
        if self.amount:
            _dict['amount'] = self.amount.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of PaymentprocessorInitPaymentRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "tenantId": obj.get("tenantId"),
            "context": PaymentprocessorPaymentContext.from_dict(obj.get("context")) if obj.get("context") is not None else None,
            "code": obj.get("code"),
            "amount": PaymentprocessorMoney.from_dict(obj.get("amount")) if obj.get("amount") is not None else None,
            "currency": obj.get("currency"),
            "additionalInfo": obj.get("additionalInfo")
        })
        return _obj


