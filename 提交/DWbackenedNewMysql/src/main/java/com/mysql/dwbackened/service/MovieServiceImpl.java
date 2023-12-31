package com.mysql.dwbackened.service;

import com.mysql.dwbackened.dto.MovieDetailDto;
import com.mysql.dwbackened.dto.MovieSearchDto;
import com.mysql.dwbackened.entity.Movie;
import com.mysql.dwbackened.mapper.*;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Set;
import java.util.stream.Collectors;

/**
 * @author wyx20
 * @version 1.0
 * @title MovieServiceImpl
 * @description
 * @create 2023/12/25 14:39
 */
@Service
public class MovieServiceImpl implements MovieService{
    @Autowired
    private MovieMapper movieMapper;
    @Autowired
    private GenreMapper genreMapper;

    @Autowired
    private DateMapper dateMapper;

    @Autowired
    private ActorMapper actorMapper;

    @Autowired
    private DirectorMapper directorMapper;

    @Autowired
    private VersionMapper versionMapper;

    @Autowired
    private ReviewMapper reviewMapper;

    @Override
    public HashMap<String, Object> getMovieCount(MovieSearchDto movieSearchDto) {
        // 数据源使用 hive
//        DataSourceUtil.setDB("db2");

        HashMap<String,Object> result=new HashMap<>();
        Set<String> movieSet=movieMapper.selectByScoreAndTitle(movieSearchDto);
        if(movieSearchDto.getGenre_name()!="") {
            movieSet.retainAll(genreMapper.selectByGenreName(movieSearchDto));
        }
        movieSet.retainAll(dateMapper.selectByTime(movieSearchDto));
        if(movieSearchDto.getActor()!="") {
            //根据演员名先获取对应演员Id集合，再遍历act表将所有演员Id在该集合中的记录保留
//            Set<Integer> actorIdList=actorMapper.selectByName(movieSearchDto);
//            movieSet.retainAll(actorMapper.selectMovieByActorId(actorIdList));
            movieSet.retainAll(actorMapper.selectByName(movieSearchDto));
        }


        if (movieSearchDto.getDirector() != "") {
            //根据导演名先获取对应导演Id集合，再遍历director表将所有导演Id在该集合中的记录保留
//            Set<Integer> directorIdList=directorMapper.selectByName(movieSearchDto);
//            movieSet.retainAll(directorMapper.selectMovieByDirectorId(directorIdList));
            movieSet.retainAll(directorMapper.selectByName(movieSearchDto));
        }
        if(movieSearchDto.getPositive()>0) {
            movieSet.retainAll(reviewMapper.selectByPositive(movieSearchDto.getPositive()));
        }

//        movieSet.retainAll(directMovieSet);
        result.put("pages",movieSet.size()/ movieSearchDto.getPer_page());
        return result;
    }

    @Override
    public HashMap<String, Object> getMovieInfo(MovieSearchDto movieSearchDto) {
        long startTime = System.currentTimeMillis();
        int start= (movieSearchDto.getPage()-1) * movieSearchDto.getPer_page();

        HashMap<String,Object> result=new HashMap<>();
        Set<String> movieSet=movieMapper.selectByScoreAndTitle(movieSearchDto);
        if(movieSearchDto.getGenre_name()!="") {
            movieSet.retainAll(genreMapper.selectByGenreName(movieSearchDto));
        }
        movieSet.retainAll(dateMapper.selectByTime(movieSearchDto));
        if(movieSearchDto.getActor()!="") {
            //根据演员名先获取对应演员Id集合，再遍历act表将所有演员Id在该集合中的记录保留
//            Set<Integer> actorIdList=actorMapper.selectByName(movieSearchDto);
//            movieSet.retainAll(actorMapper.selectMovieByActorId(actorIdList));
            movieSet.retainAll(actorMapper.selectByName(movieSearchDto));
        }
        if (movieSearchDto.getDirector() != "") {
            //根据导演名先获取对应导演Id集合，再遍历director表将所有导演Id在该集合中的记录保留
//            Set<Integer> directorIdList=directorMapper.selectByName(movieSearchDto);
//            movieSet.retainAll(directorMapper.selectMovieByDirectorId(directorIdList));
            movieSet.retainAll(directorMapper.selectByName(movieSearchDto));
        }
//        result.put("pages",movieSet.size()/ movieSearchDto.getPer_page());
        //查询情感分析正向比例符合要求的movie
        if(movieSearchDto.getPositive()>0) {
            movieSet.retainAll(reviewMapper.selectByPositive(movieSearchDto.getPositive()));
        }
        List<MovieDetailDto> movieDetailDtoList=new ArrayList<>();
        if(!movieSet.isEmpty()) {
            List<Movie> movieList = movieMapper.getMovieInfo(movieSet, start, movieSearchDto.getPer_page());
            for(Movie movie : movieList){
                MovieDetailDto movieDetailDto=new MovieDetailDto();
                if(movieSearchDto.getColumns().contains("movieId"))
                    movieDetailDto.setMovieId(movie.getMovieId());
                if(movieSearchDto.getColumns().contains("title"))
                    movieDetailDto.setMovieTitle(movie.getMovieTitle());
                if(movieSearchDto.getColumns().contains("score"))
                    movieDetailDto.setMovieScore(movie.getMovieScore());
                if(movieSearchDto.getColumns().contains("runtime"))
                    movieDetailDto.setRuntime(movie.getRuntime());
                if(movieSearchDto.getColumns().contains("positive")){
                    // 使用 DecimalFormat 类
                    java.text.DecimalFormat decimalFormat = new java.text.DecimalFormat("0.00%");
                    String positive=decimalFormat.format(movie.getReviewSentimentRate());
                    movieDetailDto.setPositive(positive);
                }
                if(movieSearchDto.getColumns().contains("date"))
                    movieDetailDto.setDate(dateMapper.selectDateByMovieId(movie.getMovieId()));
                if(movieSearchDto.getColumns().contains("directors")){
                    movieDetailDto.setDirectors(String.join(", ", directorMapper.selectNameByMovieId(movie.getMovieId())));
                }
                if(movieSearchDto.getColumns().contains("actors")){
                    movieDetailDto.setActors(String.join(", ",actorMapper.selectNameByMovieId(movie.getMovieId())));
                }
                if(movieSearchDto.getColumns().contains("format")){
                    List<String> formats = versionMapper.selectFormatByMovieId(movie.getMovieId());
                    // 使用流过滤包含 "null" 的元素，然后通过逗号连接
                    String formattedFormat = formats.stream()
                            .filter(format -> format != null && !format.equals("null"))
                            .collect(Collectors.joining(", "));
                    movieDetailDto.setFormat(String.join(", ",formattedFormat));
                }
                if(movieSearchDto.getColumns().contains("edition")){
                    movieDetailDto.setEdition(String.join(", ",versionMapper.selectEditionByMovieId(movie.getMovieId())));
                }
                if(movieSearchDto.getColumns().contains("genre")){
                    String genreName=String.join(", ",genreMapper.selectGenreByMovieId(movie.getMovieId()));
                    movieDetailDto.setGenre(genreName.replace("null",""));
                }

                movieDetailDtoList.add(movieDetailDto);
            }
        }

        result.put("data",movieDetailDtoList);

        //统计查询时间
        long queryTimeMillis = System.currentTimeMillis() - startTime;
        double queryTimeSeconds = queryTimeMillis / 1000.0; // 将毫秒转换为秒
        result.put("consuming_time",queryTimeSeconds);
        return result;
    }

    @Override
    public HashMap<String, Object> getTitleRecommend(String title, int amount) {
        HashMap<String, Object> result=new HashMap<>();
        result.put("suggestions",movieMapper.getTitleRecommend(title,amount));
        return result;
    }
}
