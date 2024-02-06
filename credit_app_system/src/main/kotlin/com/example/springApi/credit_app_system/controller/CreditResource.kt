package com.example.springApi.credit_app_system.controller

import com.example.springApi.credit_app_system.dto.CreditDto
import com.example.springApi.credit_app_system.dto.CreditView
import com.example.springApi.credit_app_system.dto.CreditViewList
import com.example.springApi.credit_app_system.dto.CustomerUpdateDto
import com.example.springApi.credit_app_system.dto.CustomerView
import com.example.springApi.credit_app_system.entity.Credit
import com.example.springApi.credit_app_system.service.impl.CreditService
import org.springframework.http.HttpStatus
import org.springframework.http.ResponseEntity
import org.springframework.web.bind.annotation.DeleteMapping
import org.springframework.web.bind.annotation.GetMapping
import org.springframework.web.bind.annotation.PatchMapping
import org.springframework.web.bind.annotation.PathVariable
import org.springframework.web.bind.annotation.PostMapping
import org.springframework.web.bind.annotation.RequestBody
import org.springframework.web.bind.annotation.RequestMapping
import org.springframework.web.bind.annotation.RequestParam
import org.springframework.web.bind.annotation.RestController
import java.util.UUID
import java.util.stream.Collectors

@RestController
@RequestMapping("/api/credits")
class CreditResource(
    private val creditService: CreditService,
) {

    @PostMapping
    fun saveCredit(@RequestBody credit: CreditDto): ResponseEntity<String> {
        val savedCredit = this.creditService.save(credit.toEntity())
        return ResponseEntity.status(HttpStatus.CREATED)
            .body(
                "Customer ${savedCredit.creditCode} - " +
                        "Customer ${savedCredit.customer?.firstName} saved with ID ${savedCredit.id} saved!"
            )
    }

    @GetMapping
    fun findAllByCustomerId(@RequestParam(value = "customerId") id: Long): ResponseEntity<List<CreditViewList>> {
        return ResponseEntity.status(HttpStatus.OK).body(
            this.creditService.findAllByCustomer(id).stream().map { credit: Credit ->
                CreditViewList(credit)
            }.collect(Collectors.toList())
        )


    }

    @GetMapping("/{creditCode}")
    fun findByCreditCode(
        @RequestParam(value = "customerId") customerId: Long,
        @PathVariable creditCode: UUID,
    ): ResponseEntity<CreditView> {
        val credit: Credit = this.creditService.findByCreditCode(customerId, creditCode)
        return ResponseEntity.status(HttpStatus.OK).body(CreditView(credit))
    }

}