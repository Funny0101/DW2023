package com.mysql.dwbackened.service;


import com.mysql.dwbackened.dto.ActorRelationCountDto;
import com.mysql.dwbackened.dto.ActorRelationInfoDto;
import com.mysql.dwbackened.mapper.ActorMapper;
import com.mysql.dwbackened.mapper.MovieMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

/**
 * @author wyx20
 * @version 1.0
 * @title ActorServiceImpl
 * @description
 * @create 2023/12/26 17:43
 */
@Service
public class ActorServiceImpl implements ActorService {

    @Autowired
    ActorMapper actorMapper;

    @Autowired
    MovieMapper movieMapper;

    @Override
    public HashMap<String, Object> getActorRecommend(String actor, int amount) {
        HashMap<String, Object> result=new HashMap<>();
        result.put("suggestions",actorMapper.getActorRecommend(actor,amount));
        return result;
    }

    /**
     * @description 查询合作次数大于五的组合总数
     * @author wyx20
     * @param[1] page
     * @param[2] perPage
     * @throws
     * @return HashMap<Object>
     * @time 2023/12/26 21:46
     */

    @Override
    public HashMap<String, Object> selectActorRelationCount(int page, int perPage) {
        HashMap<String,Object> result=new HashMap<>();
        result.put("pages",actorMapper.selectActorRelationCount().size()/perPage);
        return result;
    }


    @Override
    public HashMap<String, Object> selectActorRelationInfo(int page, int perPage) {
        long startTime = System.currentTimeMillis();
        HashMap<String,Object> result=new HashMap<>();
        int start=(page-1)*perPage;
        List<ActorRelationCountDto> actorRelationCountDtoList =actorMapper.selectActorRelationPage(start,perPage);
        List<ActorRelationInfoDto> actorRelationInfoDtoList=new ArrayList<>();
        for(ActorRelationCountDto actorRelationCountDto : actorRelationCountDtoList){
            ActorRelationInfoDto actorRelationInfoDto=new ActorRelationInfoDto();
            //查询对应人名
            actorRelationInfoDto.setName1(actorMapper.selectNameByActorId(actorRelationCountDto.getLeftPersonId()));
            actorRelationInfoDto.setName2(actorMapper.selectNameByActorId(actorRelationCountDto.getRightPersonId()));
            actorRelationInfoDto.setTimes(actorRelationCountDto.getCooperationCount());

            actorRelationInfoDtoList.add(actorRelationInfoDto);
        }
        result.put("data",actorRelationInfoDtoList);

        //统计查询时间
        long queryTimeMillis = System.currentTimeMillis() - startTime;
        double queryTimeSeconds = queryTimeMillis / 1000.0; // 将毫秒转换为秒
        result.put("consuming_time",queryTimeSeconds);
        return result;
    }

    @Override
    public HashMap<String, Object> getGenreRelationInfo(String genre) {
        long startTime = System.currentTimeMillis();
        HashMap<String,Object> result=new HashMap<>();

        List<ActorRelationCountDto> actorRelationCountDtoList =actorMapper.getGenreRelationInfo(genre);
        List<ActorRelationInfoDto> actorRelationInfoDtoList=new ArrayList<>();
        for(ActorRelationCountDto actorRelationCountDto : actorRelationCountDtoList){
            ActorRelationInfoDto actorRelationInfoDto=new ActorRelationInfoDto();
            //查询对应人名
            actorRelationInfoDto.setName1(actorMapper.selectNameByActorId(actorRelationCountDto.getLeftPersonId()));
            actorRelationInfoDto.setName2(actorMapper.selectNameByActorId(actorRelationCountDto.getRightPersonId()));
            actorRelationInfoDto.setTimes(actorRelationCountDto.getCooperationCount());

            actorRelationInfoDtoList.add(actorRelationInfoDto);
        }
        result.put("data",actorRelationInfoDtoList);

        //统计查询时间
        long queryTimeMillis = System.currentTimeMillis() - startTime;
        double queryTimeSeconds = queryTimeMillis / 1000.0; // 将毫秒转换为秒
        result.put("consuming_time",queryTimeSeconds);
        return result;
    }
}
