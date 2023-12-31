package com.mysql.dwbackened.entity;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

/**
 * @author wyx20
 * @version 1.0
 * @title Review
 * @description
 * @create 2023/12/30 20:33
 */
@Data
@AllArgsConstructor
@NoArgsConstructor
public class ReviewSentiment {
    private String movieId;
    private float sentimentScore;

}
