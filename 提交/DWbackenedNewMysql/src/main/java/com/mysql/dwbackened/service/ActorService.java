package com.mysql.dwbackened.service;

import java.util.HashMap;

/**
 * @author wyx20
 * @version 1.0
 * @title ActorService
 * @description
 * @create 2023/12/26 17:43
 */
public interface ActorService {
    HashMap<String, Object> getActorRecommend(String actor, int amount);

    HashMap<String, Object> selectActorRelationCount(int page, int perPage);

    HashMap<String, Object> selectActorRelationInfo(int page, int perPage);

    HashMap<String, Object> getGenreRelationInfo(String genre);
}
