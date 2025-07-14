package com.example.composecalculator;

import androidx.compose.foundation.horizontalScroll
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.verticalScroll
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp

@Composable
fun CalculatorScreen() {
    var equation by remember { mutableStateOf("") }
    var display by remember { mutableStateOf("") }
    var lastWasResult by remember { mutableStateOf(false) }
    var history by remember { mutableStateOf(listOf<String>()) }

    fun appendToEquation(value: String) {
        if (lastWasResult) {
            if (value in listOf("+", "-", "*", "/", "(", ")")) {
                equation = display + value
            } else {
                equation = value
            }
            lastWasResult = false
        } else {
            equation += value
        }
        display = equation
    }

    fun clear() {
        equation = ""
        display = ""
        lastWasResult = false
    }

    fun backspace() {
        if (equation.isNotEmpty()) {
            equation = equation.dropLast(1)
            display = equation
        }
    }

    fun calculate() {
        try {
            val result = evaluateExpression(equation)
            val historyEntry = "$equation = $result"
            history = (listOf(historyEntry) + history).take(10)
            display = result
            lastWasResult = true
        } catch (e: Exception) {
            display = "Error"
            lastWasResult = true
        }
    }

    Column(
        modifier = Modifier
            .fillMaxSize()
            .padding(16.dp)
    ) {
        Text(
            text = "History:",
            fontWeight = FontWeight.Bold,
            fontSize = 20.sp,
            modifier = Modifier.padding(bottom = 4.dp)
        )

        Column(
            modifier = Modifier
                .weight(1f)
                .padding(bottom = 8.dp)
                .verticalScroll(rememberScrollState())
        ) {
            for (entry in history) {
                Text(
                    text = entry,
                    fontSize = 16.sp,
                    modifier = Modifier.padding(vertical = 2.dp)
                )
            }
        }

        val scrollState = rememberScrollState()

        LaunchedEffect(display) {
            scrollState.scrollTo(scrollState.maxValue)
        }

        Box(
            modifier = Modifier
                .fillMaxWidth()
                .padding(16.dp)
                .horizontalScroll(scrollState),
            contentAlignment = Alignment.BottomEnd
        ) {
            Text(
                text = display.ifEmpty { "0" },
                fontSize = 36.sp,
                fontWeight = FontWeight.Bold,
                textAlign = TextAlign.End,
                maxLines = 1,
                softWrap = false
            )
        }

        CalculatorButtons(
            onButtonClick = { value ->
                when (value) {
                    "C" -> clear()
                    "⌫" -> backspace()
                    "=" -> calculate()
                    else -> appendToEquation(value)
                }
            }
        )
    }
}