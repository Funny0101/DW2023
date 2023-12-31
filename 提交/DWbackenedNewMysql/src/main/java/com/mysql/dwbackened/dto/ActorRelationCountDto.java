package com.mysql.dwbackened.dto;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

/**
 * @author wyx20
 * @version 1.0
 * @title ActorReleationCountDto
 * @description
 * @create 2023/12/26 21:23
 */
@Data
@AllArgsConstructor
@NoArgsConstructor
public class ActorRelationCountDto {
    private int leftPersonId;
    private int rightPersonId;
    private int cooperationCount;
}
