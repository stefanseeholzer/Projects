package com.example.legodataapp

import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.material3.Icon
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.res.painterResource
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.example.legodataapp.model.AuthViewModel
import androidx.compose.ui.graphics.Color
import com.example.legodataapp.ui.theme.Brown
import com.example.legodataapp.ui.theme.fontFamily

@Composable
fun DrawerHeader(viewModel: AuthViewModel) {
    Box(
        modifier = Modifier
            .padding(top = 100.dp)
    ) {
        Text(
            text = if (viewModel.userIsAuthenticated) "Welcome back, " +
                    "${viewModel.user.value?.name}!"
                    else "",
            color = Brown,
            fontWeight = FontWeight.Bold,
            fontSize = 18.sp,
            modifier = Modifier.padding(start = 30.dp)
        )
    }
}

@Composable
fun DrawerBody(
    items: List<NavItem>,
    modifier: Modifier = Modifier,
    contentColor: Color,
    onItemClick: (NavItem) -> Unit
) {
    LazyColumn(modifier) {
        items(items) {item ->
            Row(
                modifier = Modifier
                    .fillMaxWidth()
                    .clickable {
                        onItemClick(item)
                    }
                    .padding(25.dp)
            ) {
                Icon(
                    painter = painterResource(id = item.icon),
                    contentDescription = item.contentDescription,
                    tint = contentColor
                )
                Spacer(modifier = Modifier.width(15.dp))
                Text(
                    text = item.title,
                    color = contentColor,
                    fontSize = 20.sp,
                    fontFamily = fontFamily,
                    fontWeight = FontWeight.Bold
                )
            }
        }
    }
}