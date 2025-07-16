package com.example.legodataapp

import android.content.Context
import com.auth0.android.Auth0
import com.auth0.android.authentication.AuthenticationException
import com.auth0.android.callback.Callback
import com.auth0.android.provider.WebAuthProvider
import com.auth0.android.result.Credentials

fun Logout(
    onLogoutSuccess: () -> Unit,
    context: Context
) {
    val account = Auth0(
        "CLIENT ID",
        "DOMAIN"
    )

    WebAuthProvider
        .logout(account)
        .withScheme("app")
        .start(context, object: Callback<Void?, AuthenticationException> {
            override fun onSuccess(result: Void?) {
                onLogoutSuccess()
            }
            override fun onFailure(error: AuthenticationException) {
            }
        })
}