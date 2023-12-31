package com.mysql.dwbackened.service;

import java.util.HashMap;

/**
 * @author wyx20
 * @version 1.0
 * @title GenreService
 * @description
 * @create 2023/12/26 17:09
 */
public interface GenreService {
    HashMap<String, Object> getGenreRecommend(String genre, int amount);

}
