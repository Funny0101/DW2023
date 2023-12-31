package com.mysql.dwbackened.entity;

import com.baomidou.mybatisplus.annotation.TableId;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

/**
 * @author wyx20
 * @version 1.0
 * @title releaseDate
 * @description
 * @create 2023/12/25 8:41
 */
@Data
@AllArgsConstructor
@NoArgsConstructor
public class ReleaseDate {
    @TableId
    private Integer dateId;
    private String movieId;
    private String year;
    private String month;
    private String day;
    private String season;
    private String weekday;
    private String weekNum;
    private String date;
}
