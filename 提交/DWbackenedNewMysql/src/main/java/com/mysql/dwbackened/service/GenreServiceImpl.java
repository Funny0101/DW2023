package com.mysql.dwbackened.service;

import com.mysql.dwbackened.mapper.GenreMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.HashMap;

/**
 * @author wyx20
 * @version 1.0
 * @title GenreServiceImpl
 * @description
 * @create 2023/12/26 17:09
 */
@Service
public class GenreServiceImpl implements GenreService {

    @Autowired
    GenreMapper genreMapper;

    @Override
    public HashMap<String, Object> getGenreRecommend(String genre, int amount) {
        HashMap<String, Object> result=new HashMap<>();
        result.put("suggestions",genreMapper.getGenreRecommend(genre,amount));
        return result;
    }

}
