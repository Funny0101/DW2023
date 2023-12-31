package com.mysql.dwbackened.entity;

//import io.swagger.models.auth.In;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

/**
 * @author wyx20
 * @version 1.0
 * @title Direct
 * @description
 * @create 2023/12/25 14:03
 */
@Data
@AllArgsConstructor
@NoArgsConstructor
public class Direct {
    private String movieId;
    private Integer directorId;
}
