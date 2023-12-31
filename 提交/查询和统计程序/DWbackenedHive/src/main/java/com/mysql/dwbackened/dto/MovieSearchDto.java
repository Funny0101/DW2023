package com.mysql.dwbackened.dto;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.util.List;

/**
 * @author wyx20
 * @version 1.0
 * @title MovieCountDto
 * @description
 * @create 2023/12/25 14:32
 */
@Data
@AllArgsConstructor
@NoArgsConstructor
public class MovieSearchDto {
    private String genre_name;
    private float min_score;
    private float max_score;
    private String title;
    private String director;
    private String actor;
    private String year;
    private String month;
    private String season;
    private String weekday;
    private String day;
    private Integer page;
    private Integer per_page;
    private List<String> columns;
}
