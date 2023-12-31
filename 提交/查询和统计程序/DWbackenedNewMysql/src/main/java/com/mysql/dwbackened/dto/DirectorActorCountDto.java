package com.mysql.dwbackened.dto;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

/**
 * @author wyx20
 * @version 1.0
 * @title DirectorActorCountDto
 * @description
 * @create 2023/12/26 22:29
 */
@Data
@AllArgsConstructor
@NoArgsConstructor
public class DirectorActorCountDto {
    private int directorId;
    private int actorId;
    private int cooperationCount;
}
