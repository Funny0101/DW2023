package com.mysql.dwbackened.dto;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

/**
 * @author wyx20
 * @version 1.0
 * @title DirectorActorInfoDto
 * @description
 * @create 2023/12/26 23:07
 */
@Data
@AllArgsConstructor
@NoArgsConstructor
public class DirectorActorInfoDto {
    private String name1;
    private String name2;
    private int times;
}
