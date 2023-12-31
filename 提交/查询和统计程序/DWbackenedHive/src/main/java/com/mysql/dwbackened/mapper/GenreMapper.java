package com.mysql.dwbackened.mapper;


import com.baomidou.mybatisplus.core.mapper.BaseMapper;
import com.mysql.dwbackened.dto.MovieSearchDto;
import com.mysql.dwbackened.entity.Genre;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Select;

import java.util.List;
import java.util.Set;

/**
 * @author wyx20
 * @version 1.0
 * @title GenreMapper
 * @description
 * @create 2023/12/25 15:00
 */
@Mapper
public interface GenreMapper extends BaseMapper<Genre> {
    @Select("select movie_id from genre where  genre_name LIKE CONCAT('%', #{genre_name}, '%')")
    Set<String> selectByGenreName(MovieSearchDto movieSearchDto);

    @Select("select DISTINCT(genre_name) from genre where genre_name LIKE CONCAT('%', #{genre}, '%') LIMIT #{amount}")
    List<String> getGenreRecommend(String genre, int amount);
}
