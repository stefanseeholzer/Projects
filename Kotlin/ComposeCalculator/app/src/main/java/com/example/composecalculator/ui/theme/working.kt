/*
import androidx.compose.foundation.layout.*
import androidx.compose.material3.Button
import androidx.compose.material3.Text
import androidx.compose.runtime.*
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.example.composecalculator.Display

@Composable
fun Calculator(modifier: Modifier = Modifier) {
    var displayValue by remember { mutableStateOf("0") }
    var operand by remember { mutableStateOf<Double?>(null) }
    var pendingOperator by remember { mutableStateOf<String?>(null) }
    var lastInputWasOperator by remember { mutableStateOf(false) }
    var error by remember { mutableStateOf(false) }

    val buttonRows = listOf(
        listOf("C", "±", "%", "÷"),
        listOf("7", "8", "9", "×"),
        listOf("4", "5", "6", "−"),
        listOf("1", "2", "3", "+"),
        listOf("0", ".", "=",)
    )

    fun clear() {
        displayValue = "0"
        operand = null
        pendingOperator = null
        lastInputWasOperator = false
        error = false
    }

    fun inputNumber(num: String) {
        if (error) {
            clear()
        }
        if (lastInputWasOperator || displayValue == "0") {
            displayValue = if (num == ".") "0." else num
        } else if (num == "." && displayValue.contains(".")) {
            // Do nothing, only one decimal allowed
        } else {
            displayValue += num
        }
        lastInputWasOperator = false
    }

    fun inputOperator(op: String) {
        if (error) return
        if (!lastInputWasOperator) {
            operand = displayValue.toDoubleOrNull()
            pendingOperator = op
            lastInputWasOperator = true
        } else {
            pendingOperator = op
        }
    }

    fun calculate() {
        if (error || operand == null || pendingOperator == null) return
        val secondOperand = displayValue.toDoubleOrNull() ?: return
        val result = when (pendingOperator) {
            "+" -> operand!! + secondOperand
            "−" -> operand!! - secondOperand
            "×" -> operand!! * secondOperand
            "÷" -> if (secondOperand == 0.0) {
                error = true
                "Error"
            } else operand!! / secondOperand
            else -> secondOperand
        }
        displayValue = if (result is String) result else result.toString().removeSuffix(".0")
        operand = null
        pendingOperator = null
        lastInputWasOperator = false
    }

    fun toggleSign() {
        if (displayValue == "0" || error) return
        displayValue = if (displayValue.startsWith("-")) displayValue.drop(1) else "-$displayValue"
    }

    fun percent() {
        val value = displayValue.toDoubleOrNull() ?: return
        displayValue = (value / 100).toString()
    }

    Column(
        modifier = modifier
            .fillMaxSize()
            .padding(24.dp),
        verticalArrangement = Arrangement.Bottom
    ) {
        Display(
            inputValue = displayValue,
            modifier = Modifier
                .fillMaxWidth()
                .padding(bottom = 24.dp)
        )
        for (row in buttonRows) {
            Row(
                modifier = Modifier
                    .fillMaxWidth()
                    .padding(vertical = 4.dp),
                horizontalArrangement = Arrangement.spacedBy(8.dp)
            ) {
                for (button in row) {
                    val weight = if (button == "0") 2f else 1f
                    Button(
                        onClick = {
                            when (button) {
                                "C" -> clear()
                                "±" -> toggleSign()
                                "%" -> percent()
                                "+", "−", "×", "÷" -> inputOperator(button)
                                "=" -> calculate()
                                "." -> inputNumber(".")
                                else -> inputNumber(button)
                            }
                        },
                        modifier = Modifier
                            .weight(weight)
                            .padding(horizontal = 2.dp)
                    ) {
                        Text(
                            text = button,
                            fontSize = 28.sp
                        )
                    }
                }
            }
        }
    }
}
 */