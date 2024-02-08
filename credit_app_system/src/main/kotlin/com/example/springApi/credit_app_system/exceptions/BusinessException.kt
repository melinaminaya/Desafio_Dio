package com.example.springApi.credit_app_system.exceptions

data class BusinessException(override val message: String) : RuntimeException(message)

