package com.mysql.dwbackened.entity;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

/**
 * @author wyx20
 * @version 1.0
 * @title Act
 * @description
 * @create 2023/12/25 13:36
 */
@Data
@NoArgsConstructor
@AllArgsConstructor
public class Act {
    private String movieId;
    private Integer actorId;
    private String isMainActor;
}
