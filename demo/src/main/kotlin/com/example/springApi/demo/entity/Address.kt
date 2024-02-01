package com.example.springApi.demo.entity

import jakarta.persistence.Embeddable

@Embeddable
data class Address(
var zipCode: String = "",
    var rua : String = "",
)
