# # PaymentprocessorUpdatePaymentMethodRequest


## Properties 


Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id**| **str** |   |
**code**| **str** |   |
**title**| [**PaymentprocessorLocalizedText**](PaymentprocessorLocalizedText.md) |   | [optional]
**label**| [**PaymentprocessorLocalizedText**](PaymentprocessorLocalizedText.md) |   | [optional]
**enabled**| **bool** |   | [optional]
**amount**| [**PaymentprocessorMoney**](PaymentprocessorMoney.md) |   | [optional]
**currency**| [**PaymentprocessorCurrency**](PaymentprocessorCurrency.md) |  for more information please, see Model/PaymentprocessorCurrency.php  | [optional]
**configuration**| **object** |   | [optional]
**is_upfront**| **bool** |   | [optional]
**description**| [**PaymentprocessorLocalizedText**](PaymentprocessorLocalizedText.md) |   | [optional]
**restrictions**| [**List[PaymentprocessorPaymentMethodRestriction]**](PaymentprocessorPaymentMethodRestriction.md) |   | [optional]
**field_mask**| **str** |   | [optional]


[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)

