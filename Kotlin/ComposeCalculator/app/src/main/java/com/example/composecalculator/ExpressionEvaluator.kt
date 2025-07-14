package com.example.composecalculator

import java.util.Stack

fun evaluateExpression(expr: String): String {
    val tokens = tokenize(expr)
    val rpn = toRPN(tokens)
    val result = evalRPN(rpn)
    return if (result % 1.0 == 0.0) result.toInt().toString() else result.toString()
}

fun tokenize(expr: String): List<String> {
    val tokens = mutableListOf<String>()
    var number = ""
    for (c in expr) {
        when {
            c.isDigit() || c == '.' -> number += c
            c in "+-*/()" -> {
                if (number.isNotEmpty()) {
                    tokens.add(number)
                    number = ""
                }
                tokens.add(c.toString())
            }
            c == ' ' -> continue
            else -> throw IllegalArgumentException("Invalid character")
        }
    }
    if (number.isNotEmpty()) tokens.add(number)
    return tokens
}

fun toRPN(tokens: List<String>): List<String> {
    val output = mutableListOf<String>()
    val stack = Stack<String>()
    val precedence = mapOf(
        "+" to 1, "-" to 1,
        "*" to 2, "/" to 2
    )
    for (token in tokens) {
        when {
            token.toDoubleOrNull() != null -> output.add(token)
            token in "+-*/" -> {
                while (stack.isNotEmpty() && stack.peek() in "+-*/" &&
                    precedence[token]!! <= precedence[stack.peek()]!!
                ) {
                    output.add(stack.pop())
                }
                stack.push(token)
            }
            token == "(" -> stack.push(token)
            token == ")" -> {
                while (stack.isNotEmpty() && stack.peek() != "(") {
                    output.add(stack.pop())
                }
                if (stack.isEmpty() || stack.pop() != "(") throw IllegalArgumentException("Mismatched parenthesis")
            }
        }
    }
    while (stack.isNotEmpty()) {
        val op = stack.pop()
        if (op == "(" || op == ")") throw IllegalArgumentException("Mismatched parenthesis")
        output.add(op)
    }
    return output
}

fun evalRPN(tokens: List<String>): Double {
    val stack = Stack<Double>()
    for (token in tokens) {
        when {
            token.toDoubleOrNull() != null -> stack.push(token.toDouble())
            token in "+-*/" -> {
                val b = stack.pop()
                val a = stack.pop()
                val res = when (token) {
                    "+" -> a + b
                    "-" -> a - b
                    "*" -> a * b
                    "/" -> a / b
                    else -> throw IllegalArgumentException("Unknown operator")
                }
                stack.push(res)
            }
        }
    }
    return stack.pop()
}