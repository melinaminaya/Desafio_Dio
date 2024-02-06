package com.example.springApi.credit_app_system.dto

import com.example.springApi.credit_app_system.entity.Credit
import com.example.springApi.credit_app_system.enums.Status
import java.math.BigDecimal
import java.util.UUID

data class CreditView(
    val creditCode: UUID,
    val creditValue: BigDecimal,
    val numberOfInstallments: Int,
    val status: Status,
    val emailCustomer: String?,
    val incomeCustomer: BigDecimal?
) {
constructor(credit: Credit): this(
    creditCode = credit.creditCode, credit.creditValue, credit.numberOfInstallments, credit.status,
    credit.customer?.email, credit.customer?.income)
}
