package com.mysql.dwbackened.mapper;


import com.baomidou.mybatisplus.core.mapper.BaseMapper;
import com.mysql.dwbackened.dto.MovieSearchDto;
import com.mysql.dwbackened.entity.ReleaseDate;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Select;
import org.springframework.stereotype.Repository;

import java.util.Set;

/**
 * @author wyx20
 * @version 1.0
 * @title DateMapper
 * @description
 * @create 2023/12/25 8:50
 */
@Mapper
@Repository
public interface DateMapper extends BaseMapper<ReleaseDate> {
    @Select("SELECT COUNT(date_id) from release_date where year=#{year}")
    int selectByYear(String year);

    @Select("select movie_id from release_date where (#{year} is NULL or year=#{year}) AND (#{month} is NULL or month=#{month}) AND (#{season} is NULL or season=#{season}) AND (#{weekday} is NULL or weekday=#{weekday})")
    Set<String> selectByTime(MovieSearchDto movieSearchDto);

    @Select("SELECT `date` from release_date where movie_id=#{movieId}")
    String selectDateByMovieId(String movieId);
}
