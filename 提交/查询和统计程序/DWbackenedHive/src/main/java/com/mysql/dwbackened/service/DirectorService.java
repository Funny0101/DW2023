package com.mysql.dwbackened.service;

import java.util.HashMap;

/**
 * @author wyx20
 * @version 1.0
 * @title DirectorService
 * @description
 * @create 2023/12/26 17:28
 */
public interface DirectorService {
    HashMap<String, Object> getDirectorRecommend(String director, int amount);

    HashMap<String, Object> selectDirectorActorCount(int page, int perPage);

    HashMap<String, Object> selectDirectorActorInfo(int page, int perPage);
}
