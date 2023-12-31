package com.mysql.dwbackened.dto;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

/**
 * @author wyx20
 * @version 1.0
 * @title MovieDetailDto
 * @description
 * @create 2023/12/26 16:07
 */
@Data
@AllArgsConstructor
@NoArgsConstructor
public class MovieDetailDto {
    private String movieId;
    private String movieTitle;
//    private float movieScore;
    private String movieScore;
    private String runtime;
    private String date;
    private String directors;
    private String actors;
    private String format;
    private String edition;

}
