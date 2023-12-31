package com.mysql.dwbackened.entity;

//import io.swagger.models.auth.In;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

/**
 * @author wyx20
 * @version 1.0
 * @title genre
 * @description
 * @create 2023/12/25 14:14
 */
@Data
@AllArgsConstructor
@NoArgsConstructor
public class Genre {
    private Integer genreId;
    private String movieId;
    private String genreName;
}
