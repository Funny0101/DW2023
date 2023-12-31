package com.mysql.dwbackened.mapper;


import com.baomidou.mybatisplus.core.mapper.BaseMapper;
import com.mysql.dwbackened.entity.Version;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Select;

import java.util.List;

/**
 * @author wyx20
 * @version 1.0
 * @title VersionMapper
 * @description
 * @create 2023/12/26 19:56
 */
@Mapper
public interface VersionMapper extends BaseMapper<Version> {

    @Select("select DISTINCT(format) from version where movie_id=#{movieId}")
    public List<String> selectFormatByMovieId(String movieId);

    @Select("select DISTINCT(edition) from version where movie_id=#{movieId}")
    public List<String> selectEditionByMovieId(String movieId);
}
