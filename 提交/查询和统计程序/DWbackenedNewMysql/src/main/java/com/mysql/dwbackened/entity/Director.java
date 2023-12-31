package com.mysql.dwbackened.entity;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

/**
 * @author wyx20
 * @version 1.0
 * @title Director
 * @description
 * @create 2023/12/25 14:06
 */
@Data
@AllArgsConstructor
@NoArgsConstructor
public class Director {
    private Integer directorId;
    private String directorName;
}
