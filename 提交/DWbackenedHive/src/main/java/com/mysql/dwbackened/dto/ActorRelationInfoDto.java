package com.mysql.dwbackened.dto;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.util.List;

/**
 * @author wyx20
 * @version 1.0
 * @title ActorRelationInfoDto
 * @description
 * @create 2023/12/26 21:48
 */
@Data
@AllArgsConstructor
@NoArgsConstructor
public class ActorRelationInfoDto {
    private String name1;
    private String name2;
    private int times;
}
