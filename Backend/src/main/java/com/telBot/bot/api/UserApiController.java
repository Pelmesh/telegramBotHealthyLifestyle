package com.telBot.bot.api;

import com.telBot.bot.Repo.UserRepository;
import com.telBot.bot.model.Body;
import com.telBot.bot.model.User;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import springfox.documentation.swagger2.annotations.EnableSwagger2;

import java.util.List;

@EnableSwagger2
@RestController
@RequestMapping("/api/user")
public class UserApiController {

    @Autowired
    private UserRepository userRepository;

    @GetMapping
    public List<User> getAllUsers(){
        return  userRepository.findAll();
    }

    @GetMapping("{idChat}")
    public User getByIdChat(@PathVariable Long idChat){
        return  userRepository.findByIdChat(idChat);
    }

    @PostMapping
    public User saveUser(@RequestBody User user){
        return userRepository.save(user);
    }

}
