package tcc.superdev.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import tcc.superdev.model.Mensagens;
import tcc.superdev.repository.MensagensRepository;

import java.util.List;

@Service
public class MensagensService {
 
    @Autowired
    private MensagensRepository mensagensRepository;

    public List<Mensagens> getAllMensagens() {
        return mensagensRepository.findAll();
    }
}
