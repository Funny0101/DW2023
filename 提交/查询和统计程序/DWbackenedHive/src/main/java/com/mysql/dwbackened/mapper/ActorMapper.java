package com.mysql.dwbackened.mapper;

import com.mysql.dwbackened.dto.ActorRelationCountDto;
import com.mysql.dwbackened.dto.ActorRelationInfoDto;
import com.mysql.dwbackened.dto.MovieSearchDto;
import com.mysql.dwbackened.entity.Actor;
import com.baomidou.mybatisplus.core.mapper.BaseMapper;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Select;

import java.util.List;
import java.util.Set;

/**
 * @author wyx20
 * @version 1.0
 * @title ActorMapper
 * @description
 * @create 2023/12/25 19:08
 */
@Mapper
public interface ActorMapper extends BaseMapper<Actor> {
//    @Select("SELECT act.movie_id " +
//            "FROM act " +
//            "JOIN actor ON act.actor_id = actor.actor_id " +
//            "WHERE actor.actor_name LIKE CONCAT ('%', #{actor}, '%')")
//    Set<String> selectByName(MovieSearchDto movieSearchDto);

//    @Select("SELECT DISTINCT(actor_id) FROM actor where actor_name LIKE CONCAT('%', #{actor}, '%')")
//    Set<Integer> selectByName(MovieSearchDto movieSearchDto);
    @Select("SELECT DISTINCT(act.movie_id) FROM actor join act on act.actor_id=actor.actor_id  where actor_name LIKE CONCAT('%', #{actor}, '%')")
    Set<String> selectByName(MovieSearchDto movieSearchDto);


    @Select({
            "<script>",
            "SELECT movie_id FROM act",
            "WHERE actor_id IN",
            "<foreach item='actorId' collection='actorIdList' open='(' separator=',' close=')'>",
            "#{actorId}",
            "</foreach>",
            "</script>"
    })
    Set<String> selectMovieByActorId(Set<Integer> actorIdList);

    @Select("select DISTINCT(actor_name) from actor where actor_name LIKE CONCAT('%', #{actor}, '%') LIMIT #{amount}")
    List<String> getActorRecommend(String actor, int amount);

    @Select("select DISTINCT(actor_name) from actor join act on actor.actor_id=act.actor_id where act.movie_id=#{movieId}")
    List<String> selectNameByMovieId(String movieId);

    @Select("SELECT" +
            "    LEFT_PERSON_ID," +
            "    RIGHT_PERSON_ID," +
            "    COUNT(*) AS COOPERATION_COUNT" +
            " FROM " +
            "    actor_actor" +
            " GROUP BY " +
            "    LEFT_PERSON_ID, RIGHT_PERSON_ID " +
            "HAVING " +
            "    COUNT(*) > 5")
     List<ActorRelationCountDto> selectActorRelationCount();

    @Select("SELECT" +
            "    LEFT_PERSON_ID," +
            "    RIGHT_PERSON_ID," +
            "    COUNT(*) AS COOPERATION_COUNT" +
            " FROM " +
            "    actor_actor" +
            " GROUP BY " +
            "    LEFT_PERSON_ID, RIGHT_PERSON_ID " +
            "HAVING " +
            "    COUNT(*) > 5" +
            " ORDER BY " +
            "    COOPERATION_COUNT DESC " +
            " LIMIT #{start},#{perPage}")
    List<ActorRelationCountDto> selectActorRelationPage(int start, int perPage);

    @Select("select actor_name from actor where actor_id=#{personId} LIMIT 1")
    String selectNameByActorId(int personId);

    @Select("SELECT " +
            "    a.LEFT_PERSON_ID, " +
            "    a.RIGHT_PERSON_ID, " +
            "    SUM(m.review_num) AS reviewCount, " +
            "    COUNT(*) AS COOPERATION_COUNT " +
            "FROM " +
            "    actor_actor a " +
            "    JOIN movie m ON a.MOVIE_ID = m.movie_id " +
            "    JOIN genre g ON a.MOVIE_ID = g.movie_id " +
            "WHERE " +
            "    g.genre_name LIKE CONCAT('%', #{genre}, '%') " +
            "GROUP BY " +
            "    a.LEFT_PERSON_ID, a.RIGHT_PERSON_ID " +
            "ORDER BY " +
            "    reviewCount DESC " +
            "LIMIT 1")
    List<ActorRelationCountDto> getGenreRelationInfo(String genre);



}
