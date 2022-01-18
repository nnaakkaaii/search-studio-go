import { Module } from '@nestjs/common';
import { AppController } from './app.controller';
import { AppService } from './app.service';

// controllerやproviderを取りまとめる (依存関係の解決)
// 必ず1つ以上のmodule.tsが必要
@Module({
  imports: [],  // importsの配列の中に他のmoduleを入れると別のmoduleをimportすることが可能
  controllers: [AppController],
  providers: [AppService],
})
export class AppModule {}
