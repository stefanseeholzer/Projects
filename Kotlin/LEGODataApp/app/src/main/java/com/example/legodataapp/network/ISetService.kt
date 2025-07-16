package com.example.legodataapp.network

import com.example.legodataapp.data.AllSet
import retrofit2.Response
import retrofit2.http.GET
import retrofit2.http.Path
import retrofit2.http.Query
import com.example.legodataapp.data.ThemeResponse

private const val API_KEY = "ADD API KEY HERE"

interface ISetService {
    @GET("sets/?min_year=2014&max_year=2024")
    suspend fun getSets(
        @Query("key") key: String = API_KEY
    ): AllSet

    @GET("themes/{id}/")
    suspend fun getTheme(
        @Path("id") themeId: Int,
        @Query("key") key: String = API_KEY
    ): ThemeResponse
}