package com.mysql.dwbackened.service;



import com.mysql.dwbackened.dto.MovieSearchDto;

import java.util.HashMap;

/**
 * @author wyx20
 * @version 1.0
 * @title MovieService
 * @description
 * @create 2023/12/25 14:39
 */
public interface MovieService {
    HashMap<String, Object> getMovieCount(MovieSearchDto movieSearchDto);

    HashMap<String, Object> getMovieInfo(MovieSearchDto movieSearchDto);

    HashMap<String, Object> getTitleRecommend(String title, int amount);
}
