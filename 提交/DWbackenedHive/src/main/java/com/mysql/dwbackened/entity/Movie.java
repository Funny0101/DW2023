package com.mysql.dwbackened.entity;

import com.baomidou.mybatisplus.annotation.TableId;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

/**
 * @author wyx20
 * @version 1.0
 * @title movie
 * @description
 * @create 2023/12/25 8:31
 */
@Data
@AllArgsConstructor
@NoArgsConstructor
public class Movie {
    @TableId
    private String movieId;
    private String movieTitle;
//    private float movieScore;
//    private float imdbScore;
    private String movieScore;
    private String imdbScore;
    private String runtime;
//    private int reviewNum;
    private String reviewNum;
}
