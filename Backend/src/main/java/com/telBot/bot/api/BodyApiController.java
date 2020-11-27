package com.telBot.bot.api;


import com.telBot.bot.Repo.BodyRepository;
import com.telBot.bot.model.Body;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import springfox.documentation.swagger2.annotations.EnableSwagger2;

import java.util.List;

@EnableSwagger2
@RestController
@RequestMapping("/api/body")
public class BodyApiController {

    @Autowired
    private BodyRepository bodyRepository;

    @GetMapping
    public List<Body> getAllBody(){
        return  bodyRepository.findAll();
    }

    @GetMapping("{idChat}")
    public Body getByIdChat(@PathVariable Long idChat){
        return  bodyRepository.findByIdChat(idChat);
    }

    @PostMapping
    public Body saveBody(@RequestBody Body body){
        setAmrBmr(body);
        return  bodyRepository.save(body);
    }

    @PutMapping
    public Body updateBody(@RequestBody Body body){
        Body bodyChat = bodyRepository.findByIdChat(body.getIdChat());
        bodyChat.setHeight(body.getHeight());
        bodyChat.setWeight(body.getWeight());
        bodyChat.setAge(body.getAge());
        bodyChat.setGender(body.getGender());
        setAmrBmr(bodyChat);
        return bodyRepository.save(bodyChat);
    }

    public void setAmrBmr(Body body){
        if(body.getGender().equals("MALE")) {
            body.setBMR(88.4 + (13.4 * body.getWeight()) + (4.8 + body.getHeight()) - (5.7 * body.getAge()));
        }
        if(body.getGender().equals("FEMALE")) {
            body.setBMR(448 + (9.2 * body.getWeight()) + (3.1 + body.getHeight()) - (4.2 * body.getAge()));
        }
        body.setCalRate(body.getBMR() * body.getAMR());
    }
}
