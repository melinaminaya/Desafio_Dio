package com.example.springApi.credit_app_system.dto

import com.example.springApi.credit_app_system.entity.Credit
import java.math.BigDecimal
import java.util.UUID

data class CreditViewList(
    val creditCode: UUID,
    val creditValue: BigDecimal,
    val numberOfInstallments:Int
) {
    constructor(credit: Credit): this(credit.creditCode, credit.creditValue, credit.numberOfInstallments)
}
