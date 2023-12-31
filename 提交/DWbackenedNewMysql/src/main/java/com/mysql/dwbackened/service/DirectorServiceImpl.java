package com.mysql.dwbackened.service;


import com.mysql.dwbackened.dto.DirectorActorCountDto;
import com.mysql.dwbackened.dto.DirectorActorInfoDto;
import com.mysql.dwbackened.mapper.ActorMapper;
import com.mysql.dwbackened.mapper.DirectorMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

/**
 * @author wyx20
 * @version 1.0
 * @title DirectorServiceImpl
 * @description
 * @create 2023/12/26 17:32
 */
@Service
public class DirectorServiceImpl implements DirectorService {

    @Autowired
    private DirectorMapper directorMapper;
    @Autowired
    private ActorMapper actorMapper;

    @Override
    public HashMap<String, Object> getDirectorRecommend(String director, int amount) {
        HashMap<String, Object> result=new HashMap<>();
        result.put("suggestions",directorMapper.getDirectorRecommend(director,amount));
        return result;
    }

    @Override
    public HashMap<String, Object> selectDirectorActorCount(int page, int perPage) {
        HashMap<String,Object> result=new HashMap<>();
        result.put("pages",directorMapper.selectActorDirectorCount().size()/perPage);
        return result;
    }

    @Override
    public HashMap<String, Object> selectDirectorActorInfo(int page, int perPage) {
        long startTime = System.currentTimeMillis();
        HashMap<String,Object> result=new HashMap<>();
        int start=(page-1)*perPage;
        List<DirectorActorCountDto> directorActorCountDtoList =directorMapper.selectDirectorActorPage(start,perPage);
        List<DirectorActorInfoDto> directorActorInfoDtoList=new ArrayList<>();
        for(DirectorActorCountDto directorActorCountDto : directorActorCountDtoList){
            DirectorActorInfoDto directorActorInfoDto=new DirectorActorInfoDto();
            //查询对应人名
            directorActorInfoDto.setName1(directorMapper.selectNameByActorId(directorActorCountDto.getDirectorId()));
            directorActorInfoDto.setName2(actorMapper.selectNameByActorId(directorActorCountDto.getActorId()));
            directorActorInfoDto.setTimes(directorActorCountDto.getCooperationCount());
            directorActorInfoDtoList.add(directorActorInfoDto);
        }
        result.put("data",directorActorInfoDtoList);

        //统计查询时间
        long queryTimeMillis = System.currentTimeMillis() - startTime;
        double queryTimeSeconds = queryTimeMillis / 1000.0; // 将毫秒转换为秒
        result.put("consuming_time",queryTimeSeconds);
        return result;
    }
}
