package com.mysql.dwbackened.entity;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

/**
 * @author wyx20
 * @version 1.0
 * @title ActorActor
 * @description
 * @create 2023/12/26 20:55
 */
@Data
@AllArgsConstructor
@NoArgsConstructor
public class ActorActor {
    private int leftPersonId;
    private int rightPersonId;
    private String movieId;
}
